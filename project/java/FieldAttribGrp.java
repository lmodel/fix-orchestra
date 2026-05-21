package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Attributes of a field that be overridden by a rule
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FieldAttribGrp  {

  private String minInclusive;
  private String maxInclusive;
  private Integer implLength;
  private Integer implMinLength;
  private Integer implMaxLength;
  private String presence;
  private String value;
  private String rendering;
  private String encoding;


}