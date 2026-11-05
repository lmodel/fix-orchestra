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
  The limits on a field's value that a field, a use of it or a rule may set: range, length, presence, fixed or default value, character set and a display hint.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraFieldConstraintsV10Mixin  {

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