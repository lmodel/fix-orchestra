package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A condition that changes a field's presence, datatype or limits, or a check its value must pass.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraFieldRuleV10  {

  private OrchestraUniqueV10 fixrUnique;
  private List<String> fixrAssign;
  private String fixrWhen;
  private String fixrName;
  private String fixrType;
  private String fixrMinInclusive;
  private String fixrMaxInclusive;
  private Integer fixrImplLength;
  private Integer fixrImplMinLength;
  private Integer fixrImplMaxLength;
  private String fixrPresence;
  private String fixrEncoding;
  private String fixrValue;
  private String fixrRendering;


}