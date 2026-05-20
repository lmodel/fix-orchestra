package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class FieldRuleType  {

  private UniqueInline unique;
  private String when;
  private List<String> assign;
  private String name;
  private String type;
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